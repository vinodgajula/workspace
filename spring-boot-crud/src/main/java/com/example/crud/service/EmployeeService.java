package com.example.crud.service;

import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;
import java.util.Set;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.crud.dto.EmployeeUpdateRequest;
import com.example.crud.entity.Employee;
import com.example.crud.repository.EmployeeRepository;

import jakarta.validation.ConstraintViolation;
import jakarta.validation.Validator;

@Service
public class EmployeeService {

    private static final Logger logger = LoggerFactory.getLogger(EmployeeService.class);

    @Autowired
    private EmployeeRepository repository;

    @Autowired
    private Validator validator;

    public List<Employee> getAllEmployees() {
        logger.info("Fetching all employees from database.");
        return repository.findAll();
    }

    public Optional<Employee> getEmployeeById(Long id) {
        logger.info("Fetching employee by id: {}", id);
        return repository.findById(id);
    }

    public Employee saveEmployee(Employee employee) {
        employee.setInsertedDate(LocalDateTime.now());
        logger.info("Saving new employee: {}", employee.getName());
        return repository.save(employee);
    }

    public Employee updateEmployee(Long id, EmployeeUpdateRequest updatedEmployee) {
        logger.info("Updating employee with id: {}", id);
        return repository.findById(id).map(employee -> {
            if (updatedEmployee.getName() != null && !updatedEmployee.getName().isEmpty() ) {
                employee.setName(updatedEmployee.getName());
            }
            if (updatedEmployee.getRole() != null && !updatedEmployee.getRole().isEmpty()) {
                employee.setRole(updatedEmployee.getRole());
            }
            if (updatedEmployee.getSalary() != null) {
                //validateField(updatedEmployee.getSalary(), "Salary");
                employee.setSalary(updatedEmployee.getSalary());
            }
            employee.setUpdatedDate(LocalDateTime.now());
            logger.info("Successfully updated employee with id: {}", id);
            return repository.save(employee);
        }).orElseThrow(() -> {
            logger.error("Employee with id {} not found.", id);
            //throw new RuntimeException("Employee not found with id: " + id);
            return new RuntimeException("Employee not found with id: " + id);
        });
    }

    public void deleteEmployee(Long id) {
        if (!repository.existsById(id)) {
            logger.error("Failed to delete. Employee with id {} not found.", id);
            throw new RuntimeException("Employee not found with id: " + id);
        }
        logger.info("Deleting employee with id: {}", id);
        repository.deleteById(id);
    }
    
    private <T> void validateField(T value, String fieldName) {
        Set<ConstraintViolation<T>> violations = validator.validate(value);
        if (!violations.isEmpty()) {
            StringBuilder errorMessage = new StringBuilder();
            for (ConstraintViolation<T> violation : violations) {
                errorMessage.append(violation.getMessage()).append("; ");
            }
            throw new IllegalArgumentException("Validation failed for " + fieldName + ": " + errorMessage);
        }
    }
}
