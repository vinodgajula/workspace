CREATE TABLE IF NOT EXISTS messages (sender TEXT, receiver TEXT, timestamp BIGINT, id UUID, content TEXT, PRIMARY KEY ((sender, receiver), timestamp)) WITH CLUSTERING ORDER BY (timestamp ASC);
