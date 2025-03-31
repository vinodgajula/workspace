package com.chatapp.repository;

import java.util.List;
import java.util.Optional;

import org.springframework.data.cassandra.repository.CassandraRepository;
import org.springframework.stereotype.Repository;

import com.chatapp.model.User;

@Repository
public interface UserRepository extends CassandraRepository<User, String> {
    Optional<User> findByUsername(String username);
    List<User> findAll(); // New method for fetching all users
}