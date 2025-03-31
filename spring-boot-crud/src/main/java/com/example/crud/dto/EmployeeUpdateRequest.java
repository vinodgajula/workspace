package com.example.crud.dto;

import jakarta.validation.constraints.Min;

public class EmployeeUpdateRequest {

    private String name;

    private String role;

    @Min(value = 10000, message = "Salary must be at least 10000")
    private Double salary;

    // Getters and Setters
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getRole() {
        return role;
    }

    public void setRole(String role) {
        this.role = role;
    }

    public Double getSalary() {
        return salary;
    }

    public void setSalary(Double salary) {
        this.salary = salary;
    }
}
