package com.example.crud.controller;

import java.util.List;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.crud.dto.EmployeeUpdateRequest;
import com.example.crud.entity.Employee;
import com.example.crud.service.EmployeeService;

import jakarta.validation.Valid;

@RestController
@RequestMapping("/employees")
public class EmployeeController {

    private static final Logger logger = LoggerFactory.getLogger(EmployeeController.class);

    @Autowired
    private EmployeeService service;

    @GetMapping
    public List<Employee> getAllEmployees() {
        logger.info("Fetching all employees.");
        return service.getAllEmployees();
    }

    @GetMapping("/{id}")
    public ResponseEntity<Employee> getEmployeeById(@PathVariable Long id) {
        logger.info("Fetching employee with id: {}", id);
        return service.getEmployeeById(id)
                .map(ResponseEntity::ok)
                .orElseGet(() -> {
                    logger.warn("Employee with id {} not found.", id);
                    return ResponseEntity.notFound().build();
                });
    }

    @PostMapping
    public Employee createEmployee(@Valid @RequestBody Employee employee) {
        logger.info("Creating new employee: {}", employee.getName());
        return service.saveEmployee(employee);
    }

    @PutMapping("/{id}")
    public ResponseEntity<Employee> updateEmployee(@PathVariable Long id, @Valid @RequestBody EmployeeUpdateRequest employee) {
        logger.info("Updating employee with id: {}", id);
        return ResponseEntity.ok(service.updateEmployee(id, employee));
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteEmployee(@PathVariable Long id) {
        logger.info("Deleting employee with id: {}", id);
        service.deleteEmployee(id);
        return ResponseEntity.noContent().build();
    }
}
