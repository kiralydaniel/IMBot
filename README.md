# IMBot
## Description
Simple bot created in Python for personal use. 
It helps creating roster for boosts, managing player balance in a game called World of Warcraft.

## Commands

### User commands:
Everyone is able to use these commands.

```
!b - Sends user balance in private message
```
![!b image](https://i.imgur.com/Z7x1mB8.png)
```
!char - Update user payment character in Balance sheet
```
![!char image](https://i.imgur.com/QhuLmqp.png)

### Admin commands:
Only users with admin permission can use these commands.

```
!update1 - Read player names from friday.txt and insert them into Friday Boost name column
!update2 - Read player names from saturday.txt and insert them into Saturday Boost name column
```
![!update1 image](https://i.imgur.com/Uf8XC2s.png)


```
!balance1 - Update user balance based on Friday Boost sheet data
!balance2 - Update user balance based on Saturday Boost sheet data
```
![!balance1 image](https://i.imgur.com/TR0Divy.png)

```
!roster1 - Read names from Friday Boost sheet and writes a message in Discord with mentioning everyone and placing class icons in front of names
!roster2 - Read names from Saturday Boost sheet and writes a message in Discord with mentioning everyone and placing class icons in front of names
```
![!roster1 image](https://i.imgur.com/YqLoo9E.png)

```
!inv - Send message to every user that is in the Friday or Saturday Boost sheet depending on the argument.

Current arguments: friday, saturday
```
![!inv1 image](https://i.imgur.com/WQg0Kpb.png)
