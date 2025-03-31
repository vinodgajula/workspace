import React, { useState, useEffect } from "react";
import axios from "axios";
import "./App.css";
import LoginForm from "./LoginForm";
import RegisterForm from "./RegisterForm";
import MessageList from "./MessageList";
import MessageInput from "./MessageInput";
import UserList from "./UserList";

const App = () => {
  const [messages, setMessages] = useState([]);
  const [users, setUsers] = useState([]);
  const [currentUser, setCurrentUser] = useState("");
  const [selectedUser, setSelectedUser] = useState("");
  const [auth, setAuth] = useState({ token: "" });
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [showRegister, setShowRegister] = useState(false);

  // Fetch users when logged in
  useEffect(() => {
    if (isLoggedIn) {
      fetchUsers();
    }
  }, [isLoggedIn]);

  const fetchUsers = async () => {
    try {
      const response = await axios.get("http://localhost:8080/api/users", {
        headers: { Authorization: `Bearer ${auth.token}` },
      });
      setUsers(response.data);
      if (response.data.length > 0 && !selectedUser) {
        setSelectedUser(response.data[0].username);
      }
    } catch (error) {
      console.error("Error fetching users:", error);
    }
  };

  const fetchMessages = async () => {
    if (!currentUser || !selectedUser) return;
    
    try {
      const response = await axios.get("http://localhost:8080/chat/messages", {
        headers: { Authorization: `Bearer ${auth.token}` },
        params: { user1: currentUser, user2: selectedUser },
      });
      setMessages(response.data);
    } catch (error) {
      console.error("Error fetching messages:", error);
    }
  };

  const sendMessage = async (content) => {
    try {
      const message = { 
        sender: currentUser, 
        receiver: selectedUser, 
        timestamp: Date.now(), 
        content 
      };
      await axios.post("http://localhost:8080/chat/send", message, {
        headers: { Authorization: `Bearer ${auth.token}` },
      });
      fetchMessages();
    } catch (error) {
      console.error("Error sending message:", error);
    }
  };

  const handleLogin = async (username, password) => {
    try {
      const response = await axios.post("http://localhost:8080/auth/login", { 
        username, 
        password 
      });
      setAuth({ token: response.data.token });
      setCurrentUser(username);
      setIsLoggedIn(true);
    } catch (error) {
      console.error("Login failed", error);
    }
  };

  return (
    <div className="App">
      <h1>Chat App</h1>
      {isLoggedIn ? (
        <div className="chat-container">
          <div className="sidebar">
            <h2>Users</h2>
            <UserList 
              users={users} 
              currentUser={currentUser}
              selectedUser={selectedUser}
              onSelectUser={setSelectedUser}
            />
          </div>
          <div className="chat-area">
            <div className="chat-header">
              <h2>Chat with {selectedUser}</h2>
              <button onClick={fetchMessages}>Refresh</button>
            </div>
            <MessageList messages={messages} currentUser={currentUser} />
            <MessageInput sendMessage={sendMessage} />
          </div>
        </div>
      ) : showRegister ? (
        <RegisterForm 
          onRegisterSuccess={() => setShowRegister(false)} 
        />
      ) : (
        <>
          <LoginForm onLogin={handleLogin} />
          <button onClick={() => setShowRegister(true)}>Register</button>
        </>
      )}
    </div>
  );
};

export default App;