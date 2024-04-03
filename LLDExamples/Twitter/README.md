# Twitter System Design README

Welcome to the Twitter System Design README! This document provides an overview of the design considerations, functional and non-functional requirements, key insights, and system architecture of the Twitter platform.

## Functional Requirements

Twitter is a social media platform that allows users to perform various actions, including:

- **Tweeting:** Users can post short messages, images, or videos to their followers.
- **Retweeting:** Users can share tweets posted by other users with their followers.
- **Following:** Users can subscribe to updates from other users.
- **Content Search:** Users can search for tweets and users based on keywords or hashtags.

## Non-functional Requirements

To ensure a smooth user experience, Twitter must meet certain non-functional requirements, such as:

- **Read-heavy traffic:** Twitter experiences high volumes of read requests due to its large user base and tweet activity.
- **Fast rendering:** Tweets and user profiles should load quickly to provide a seamless browsing experience.
- **Low latency:** Responses to user actions, such as tweeting or following, should occur without significant delay.
- **High availability:** The Twitter platform should be accessible to users with minimal downtime.

### Scale Numbers:

Twitter operates at a massive scale, handling millions of users and tweets daily:

- **Daily Active Users (DAU):** 150 million
- **Monthly Active Users (MAU):** 350 million
- **Total User Accounts:** 1.5 billion
- **Tweets per Day:** 500 million

### Calculations:

1. **Average Tweets per DAU:**
   - Average tweets per DAU = Tweets per Day / DAU
   - Average tweets per DAU ≈ 500,000,000 / 150,000,000 ≈ 3.33

2. **Average Tweets per MAU:**
   - Average tweets per MAU = Tweets per Day / MAU
   - Average tweets per MAU ≈ 500,000,000 / 350,000,000 ≈ 1.43

### Queries Per Second (QPS):

Considering a read-to-write ratio of 10:1:

1. **Read QPS:**
   - Read QPS ≈ (DAU * (Tweets per Day / DAU + Other Read Operations)) / (24 * 3600)
   - Assuming 5 read operations per user per day:
   - Read QPS ≈ (150,000,000 * (3.33 + 5)) / (24 * 3600) ≈ 11,574

2. **Write QPS:**
   - Write QPS ≈ Tweets per Day / (24 * 3600)
   - Write QPS ≈ 500,000,000 / (24 * 3600) ≈ 5,787

## Database Choices and Recommendations

Given the massive scale and read-heavy nature of Twitter's traffic, the choice of databases is critical for performance, scalability, and reliability. Here are some recommendations:

1. **Primary Database (for Relational Data):**
   - Robust relational database management systems (RDBMS) like MySQL or PostgreSQL would be suitable. They offer excellent performance, ACID compliance, and support for complex queries.

2. **Caching Layer:**
   - Implement a caching layer using Redis or Memcached to reduce the load on the primary database by serving frequently accessed data directly from memory.

3. **Scaling Strategy:**
   - Employ horizontal scaling techniques like sharding and replication to distribute the load across multiple database instances or shards.

4. **Data Partitioning:**
   - Implement effective data partitioning strategies (e.g., range-based or hash-based) to distribute data evenly across database shards based on access patterns.

5. **Data Consistency:**
   - Use eventual consistency models for non-critical data and strong consistency for critical operations to maintain data integrity and meet real-time requirements.

In summary, choosing a robust RDBMS for relational data storage, implementing a caching layer for read-heavy traffic, and employing effective scaling and partitioning strategies are essential for meeting Twitter's massive scale and performance requirements.


## User Categorization

Users on Twitter can be categorized into different types based on their activity level:

- **Famous:** Users with a large following and high engagement.
- **Active:** Users who frequently post and engage with content.
- **Live:** Users who are currently active on the platform.
- **Passive:** Users who consume content but do not actively engage.
- **Inactive:** Users who have stopped using the platform.

## Overall System Architecture

The Twitter platform is designed using the following architectural components:

- **User Service:** Manages user authentication, profiles, and settings.
- **Graph Service:** Handles connections between users, such as followers and followees.
- **MySQL:** Stores relational data, such as user profiles and tweets.
- **Redis Cache:** Provides caching for efficient read operations, reducing latency and network bandwidth usage.

## Key Insights

- Support for functional requirements like tweeting, retweeting, following, and content search enhances user experience.
- Non-functional requirements like read-heavy traffic, fast rendering, low latency, and high availability are crucial for Twitter's success.
- Understanding user behavior and categorizing users helps tailor the platform's features and interactions.
- Caching plays a vital role in optimizing system performance, especially in read-heavy environments like Twitter.