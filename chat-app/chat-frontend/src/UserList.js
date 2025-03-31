import React from "react";

const UserList = ({ users, currentUser, selectedUser, onSelectUser }) => {
  return (
    <ul className="user-list">
      {users
        .filter(user => user.username !== currentUser)
        .map(user => (
          <li 
            key={user.username} 
            className={selectedUser === user.username ? "active" : ""}
            onClick={() => onSelectUser(user.username)}
          >
            {user.username}
            <span className="email">{user.email}</span>
          </li>
        ))}
    </ul>
  );
};

export default UserList;