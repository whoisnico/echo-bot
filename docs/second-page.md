# Commands & Features

## Basic Conmmands

### /serverinfo

> usage: `/serverinfo` 

Get following Information from the guild:
```
  Server Name
  Server ID
  Owner
  Creation Date
  Verification Level (High/Medium/Low)
  Member Count
  Server Features
  ```

### /userinfo

> usage: `/serverinfo (Member[Optional])` 

If Member = None is Member = Author  
Get following Information from the Member:
```
Username
Displayname
Status
Online
User ID
Account Created Date
Joined Server Date
Activity (Playing:Name/Streaming:Name[URL]/Listening:Song[Artist][Album])
Profile Badges (staff/partner/hypesquad/bug_hunter/hypesquad_bravery/hypesquad_brilliance/hypesquad_balance/early_supporter/system/bug_hunter_level_2/verified_bot/verified_bot_developer/early_verified_bot_developer/moderator_programs_alumni/discord_certified_moderator/http_interactions_bot/spammer/active_developer/bot)
  ```

### /botinfo

> usage: `botinfo` 

Get following Information from the Bot:
```
UpTime (Days, Hours, Minutes)
Displayname
User ID
Status (Online/Dnb/Idle/Offline)
Ping
Servers
Last Update
Importants Links
  ```

## Modmail

#### When a user send a dm to the Bot. You get the message on the `#modmail` (create the channel if you dont have it) Channel.

### /mod_answer

> usage: `/mod_answer (answer_id) (message)` \
>  Info: Answer a Modmail

You can find the **answer_id** on the footer of the embed in the modmail message. The user will get back the message and the name of the staff in the footer.