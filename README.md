# IMBot
## Description
Simple bot created in Python for personal use. 
It helps creating roster for boosts, managing player balance in a game called World of Warcraft.

## Commands

### User commands:
Everyone is able to use these commands in a channel called **#bot**.
**Current arguments: friday, saturday**

```
!b - Sends user balance in private message
```
![!b image](https://i.imgur.com/Z7x1mB8.png)<br/><br/>
```
!char - Update user payment character in Balance sheet
```
![!char image](https://i.imgur.com/QhuLmqp.png)<br/><br/>

### Admin commands:
Only users with admin permission can use these commands.


```
!update {argument} - Read player names from {argument}.txt and insert them into {argument} Boost name column
```
![!update1 image](https://i.imgur.com/Uf8XC2s.png)<br/><br/>


```
!balance - Update user balance based on {argument} Boost sheet data
```
![!balance1 image](https://i.imgur.com/TR0Divy.png)<br/><br/>


```
!roster {argument} - Read names from {argument} Boost sheet and writes a message in Discord with mentioning everyone and placing class icons in front of names
```
![!roster1 image](https://i.imgur.com/YqLoo9E.png)<br/><br/>

```
!inv - Send message to every user that is in the Friday or Saturday Boost sheet depending on the argument.
```
![!inv1 image](https://i.imgur.com/WQg0Kpb.png)<br/><br/>


```
!reset_message_store - Resets the message store for the !update_lb command.
```
