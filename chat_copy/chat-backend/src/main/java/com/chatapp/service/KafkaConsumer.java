package com.chatapp.service;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Service;

import com.chatapp.model.Message;
import com.chatapp.model.MessageStatus;
import com.chatapp.repository.MessageRepository;
import com.fasterxml.jackson.databind.ObjectMapper;

@Service
public class KafkaConsumer {

    private static final Logger logger = LoggerFactory.getLogger(KafkaConsumer.class);

    @Autowired
    private ObjectMapper objectMapper;

    @Autowired
    private MessageRepository messageRepository;

    @KafkaListener(topics = "chat-messages", groupId = "chat-group")
    public void consume(String jsonMessage) {
        try {
            // 🔄 Convert JSON string back to Message object
            Message message = objectMapper.readValue(jsonMessage, Message.class);

            logger.info("📩 Received Message: {}", message.getContent());

            // ✅ Update status to DELIVERED
            message.setStatus(MessageStatus.DELIVERED);

            // 💾 Save updated message
            messageRepository.save(message);

        } catch (Exception e) {
            logger.error("❌ Error processing message: ", e);
        }
    }
}
