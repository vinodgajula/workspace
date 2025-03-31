package com.example.crud.exception;

import java.util.HashMap;
import java.util.Map;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.FieldError;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

@RestControllerAdvice
public class GlobalExceptionHandler {

    // Logger for this class
    private static final Logger logger = LoggerFactory.getLogger(GlobalExceptionHandler.class);

    /**
     * Handles validation exceptions (e.g., @Valid failures) and returns a
     * structured response with field-specific error messages.
     *
     * @param ex MethodArgumentNotValidException
     * @return ResponseEntity with field-specific validation errors
     */
    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<Map<String, String>> handleValidationExceptions(MethodArgumentNotValidException ex) {
        // Log the validation exception
        logger.error("Validation error occurred: {}", ex.getMessage());

        Map<String, String> errors = new HashMap<>();
        // Extract field-specific error messages
        for (FieldError error : ex.getBindingResult().getFieldErrors()) {
            errors.put(error.getField(), error.getDefaultMessage());
            // Log each field error
            logger.warn("Field error - Field: {}, Message: {}", error.getField(), error.getDefaultMessage());
        }

        // Log the final response being returned
        logger.debug("Returning validation error response: {}", errors);
        return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(errors);
    }

    /**
     * Handles any other unhandled exceptions in the application and provides
     * a generic error response.
     *
     * @param ex Exception
     * @return ResponseEntity with a generic error message
     */
    @ExceptionHandler(Exception.class)
    public ResponseEntity<Map<String, String>> handleGenericExceptions(Exception ex) {
        // Log the unexpected exception
        logger.error("Unexpected error occurred: {}", ex.getMessage(), ex);

        Map<String, String> errorResponse = new HashMap<>();
        errorResponse.put("error", "An unexpected error occurred");
        errorResponse.put("details", ex.getMessage()); // Include specific exception message

        // Log the final response being returned
        logger.debug("Returning generic error response: {}", errorResponse);
        return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(errorResponse);
    }
}