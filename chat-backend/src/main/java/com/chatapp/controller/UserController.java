package com.chatapp.controller;

import com.chatapp.dto.UserDTO;
import com.chatapp.model.User;
import com.chatapp.service.UserService;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/api/users")
public class UserController {

    private final UserService userService;

    public UserController(UserService userService) {
        this.userService = userService;
    }

    @GetMapping
    public List<UserDTO> getAllUsersExceptCurrent(@AuthenticationPrincipal User currentUser) {
        return userService.findAllExceptCurrent(currentUser.getUsername());
    }
}