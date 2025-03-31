package com.chatapp.service;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.chatapp.model.Message;
import com.chatapp.repository.MessageRepository;

@Service
public class MessageService {

    @Autowired
    private MessageRepository messageRepository;

    @Autowired
    private KafkaProducer kafkaProducer;
    
    public void sendMessage(Message message) {
        kafkaProducer.sendMessage(message);
        messageRepository.save(message);
    }

    public List<Message> getMessagesBetween(String user1, String user2) {
        List<Message> list1 = messageRepository.findBySenderAndReceiver(user1, user2);
        List<Message> list2 = messageRepository.findBySenderAndReceiver(user2, user1);
    
        List<Message> allMessages = new ArrayList<>();
        allMessages.addAll(list1);
        allMessages.addAll(list2);
    
        // Optional: sort messages by timestamp 
        allMessages.sort(Comparator.comparingLong(Message::getTimestamp));
        return allMessages;
    }
}
