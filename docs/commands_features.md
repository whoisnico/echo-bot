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
## Sellpass Intergration

#### To start do you need a working Sellpass Shop and your Account API Key. This is how to get your API Key:
- Go to https://dashboard.sellpass.io/settings/security 
- Scroll down till you see API Key
- Click on Copy
- Set your Token (/setshop_token) and (/setshop_id)

## /setshop_token
> usage: `/setshop_token (token)` \
>  Connect the Bot with your Sellpass Account

You get following Information for the next Command:
```
Shop ID: 1234 - Name: Example 1
Shop ID: 4321 - Name: Example 2
```

## /setshop_id
> usage: `/setshop_id (id)` \
>  Connect the Bot with your Sellpass Shop

## /setshop_customer_role
> usage: `/setshop_customer_role (role)` \
>  Select a role for your Sellpass customers!

## /shop_claimrole
> usage: `/shop_claimrole (orderid)` \
>  Get your customer role (connected to sellpass.io)

## Tools Conmmands

## Modmail

#### When a user send a dm to the Bot. You get the message on the `#modmail` (create the channel if you dont have it) Channel.

### /mod_answer

> usage: `/mod_answer (answer_id) (message)` \
>  Info: Answer a Modmail

You can find the **answer_id** on the footer of the embed in the modmail message. The user will get back the message and the name of the staff in the footer.