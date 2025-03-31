import React from "react";

const MessageList = ({ messages, currentUser }) => {
  return (
    <div className="message-list">
      <ul>
        {messages.map((message) => (
          <li 
            key={message.id} 
            className={message.sender === currentUser ? "sent" : "received"}
          >
            <div className="message-content">
              {message.sender === currentUser ? "You" : message.sender}: {message.content}
            </div>
            <div className="message-time">
              {new Date(message.timestamp).toLocaleString()}
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default MessageList;