Below is the incident report for the Distributed Denial of Service outage that occurred on April 30, 2022. We understand this service outage has impacted our valued developers and users, and we apologize to everyone who was affected.

Issue Summary
From 10:30 AM to 11:00 AM , requests to our website resulted in an error 503 message. This rendered our website inaccessible to our normal users. This issue affected 80% traffic into our websites with just a few able to access the service. The root cause of this outage was caused by a Distributed Denial Of Service attack that led to our website inaccessible to normal users.

Timeline(East Africa Time)
10:30 AM: outrage began.
10:35 AM: system monitors alert team.
10:40 AM: networking team takes over to address the issue.
10:50 AM: Traffic restored and servers restarted.
11:00 AM: 100% traffic back online.

Root cause and Resolution
At 10:30AM our system was invaded by an anonymous amount of traffic coming from a single IP address which led to a flood of our traffic blocking a large number of normal users from accessing services. Majority of them got an Error 503 message as they tried accessing services.
At 10:35, the monitoring systems alerted our engineers who investigated and quickly escalated the issue. By 10:40 AM, the incident response team identified that the monitoring system was exacerbating the problem caused by Denial of service attack and contacted the networking team. The networking team checked the network configuration and implemented an IP-based Access Control List to block traffic coming from the attack source.
By 10:50 AM traffic was restored and servers had to be restarted and by 11:00 AM everything was completely running fine and traffic was 100% restored to normal users.

Corrective and preventative
Recently, the devops team, networking team and executive board did an internal examination of the entire system in relation to the outage we experienced and came up with the below suggestion.
Adding bandwidth monitoring that watches inbound and outbound data transfers which shall help know IP that are using most of the server traffic.
Development of CDN system that shall ensure the system is redundant in a vast geographical region with a main aim of ensuring service availability by sharing the load equally across a number of servers that are geographically distributed and closer in proximity to users.

