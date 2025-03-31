package com.chatapp.model;

import java.util.UUID;

import org.springframework.data.cassandra.core.mapping.Column;
import org.springframework.data.cassandra.core.mapping.PrimaryKeyColumn;
import org.springframework.data.cassandra.core.mapping.Table;
import org.springframework.data.cassandra.core.cql.PrimaryKeyType;
import org.springframework.data.cassandra.core.cql.Ordering;

@Table("messages")
public class Message {

    @PrimaryKeyColumn(name = "sender", type = PrimaryKeyType.PARTITIONED)
    private String sender;

    @PrimaryKeyColumn(name = "receiver", type = PrimaryKeyType.PARTITIONED)
    private String receiver;

    @PrimaryKeyColumn(name = "timestamp", ordinal = 0, type = PrimaryKeyType.CLUSTERED, ordering = Ordering.ASCENDING)
    private long timestamp;

    @Column("id")
    private UUID id = UUID.randomUUID();

    @Column("content")
    private String content;

    @Column("status")
    private MessageStatus status = MessageStatus.SENT;

    public Message() {}

    public Message(String sender, String receiver, long timestamp, String content) {
        this.sender = sender;
        this.receiver = receiver;
        this.timestamp = timestamp;
        this.content = content;
        this.id = UUID.randomUUID();
        this.status = MessageStatus.SENT;
    }

    // Getters and Setters
    public String getSender() { return sender; }
    public void setSender(String sender) { this.sender = sender; }

    public String getReceiver() { return receiver; }
    public void setReceiver(String receiver) { this.receiver = receiver; }

    public long getTimestamp() { return timestamp; }
    public void setTimestamp(long timestamp) { this.timestamp = timestamp; }

    public UUID getId() { return id; }
    public void setId(UUID id) { this.id = id; }

    public String getContent() { return content; }
    public void setContent(String content) { this.content = content; }

    public MessageStatus getStatus() { return status; }
    public void setStatus(MessageStatus status) { this.status = status; }
}
