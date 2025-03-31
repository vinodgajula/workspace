package com.chatapp.service;

import java.util.List;
import java.util.Optional;
import java.util.UUID;
import java.util.stream.Collectors;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

import com.chatapp.dto.UserDTO;
import com.chatapp.model.User;
import com.chatapp.repository.UserRepository;

@Service
public class UserService implements UserDetailsService {

    private static final Logger logger = LoggerFactory.getLogger(UserService.class);

    @Autowired
    private UserRepository userRepository;

    @Autowired
    private PasswordEncoder passwordEncoder;

    public String registerUser(User user) {
        try {
            Optional<User> existingUser = userRepository.findByUsername(user.getUsername());
            if (existingUser.isPresent()) {
                logger.warn("⚠️ Username '{}' already exists!", user.getUsername());
                return "Username already exists!";
            }

            user.setId(UUID.randomUUID().toString());
            user.setPassword(passwordEncoder.encode(user.getPassword()));
            userRepository.save(user);
            logger.info("✅ User '{}' registered successfully!", user.getUsername());
            return "User registered successfully!";
        } catch (Exception e) {
            logger.error("❌ Error registering user: {}", e.getMessage(), e);
            throw new RuntimeException("Registration failed, please try again.");
        }
    }

    public Optional<User> findByUsername(String username) {
        return userRepository.findByUsername(username);
    }

    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        try {
            return userRepository.findByUsername(username)
                    .orElseThrow(() -> new UsernameNotFoundException("User not found: " + username));
        } catch (UsernameNotFoundException e) {
            logger.warn("⚠️ User '{}' not found!", username);
            throw e;
        } catch (Exception e) {
            logger.error("❌ Unexpected error while loading user '{}': {}", username, e.getMessage(), e);
            throw new RuntimeException("Failed to load user details.");
        }
    }
    public List<UserDTO> findAllExceptCurrent(String currentUsername) {
        List<User> allUsers = userRepository.findAll();
        return allUsers.stream()
                .filter(user -> !user.getUsername().equals(currentUsername))
                .map(user -> new UserDTO(user.getUsername(), user.getEmail()))
                .collect(Collectors.toList());
    }
}
