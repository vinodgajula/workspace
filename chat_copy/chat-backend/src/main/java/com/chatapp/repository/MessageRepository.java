package com.chatapp.repository;

import java.util.List;
import java.util.UUID;

import org.springframework.data.cassandra.repository.CassandraRepository;
import org.springframework.stereotype.Repository;

import com.chatapp.model.Message;

@Repository
public interface MessageRepository extends CassandraRepository<Message, UUID> {
    List<Message> findBySenderAndReceiver(String sender, String receiver);

    // Optional: find messages between a timestamp range
    List<Message> findBySenderAndReceiverAndTimestampGreaterThanEqualAndTimestampLessThanEqual(
        String sender, String receiver, long start, long end);
}
