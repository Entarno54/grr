import selfcord
import requests
import json
import os
from kandinsky import Kandinsky
import wikipedia

bot = selfcord.Bot()

dir = os.getcwd()

blacklist = ["1136375460373221487"]

async def gsearch(query):
    API_KEY = "AIzaSyDzjqXAAyt-J4mdKG1cYYFl9qoQdSBGXUQ"
    SEARCH_ENGINE_ID = "b5d5487e5b1ea4f62"
    page = 1
    al = 0
    start = (page - 1) * 10 + 1
    url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}"
    print(query)
    data = requests.get(url).json()

    search_items = data.get("items")
    st = ""
    for i, search_item in enumerate(search_items, start=1):
        if al < 3:
            al += 1
            try:
                long_description = search_item["pagemap"]["metatags"][0]["og:description"]
            except KeyError:
                long_description = "N/A"

            title = search_item.get("title")
            snippet = search_item.get("snippet")
            link = search_item.get("link")
            st += f"\n# {title} \n## {long_description} \n### {snippet} \n{link}"
            print(st)
    return st.encode("utf8").decode("utf8")


generatingimage = False
fil = open(f"{dir}/data/users.json", "r")
base = json.loads(fil.read())
fil.close()
print(base)
pipe = Kandinsky(auth_token='eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJUeUFOUUV0TkFsZ0pjaWNfcE01ZTBwV3pWbXUyNG1zV0dLa2h1OXZpbzFFIn0.eyJleHAiOjE2OTkzNTQ2MjUsImlhdCI6MTY5ODA1ODYyNSwiYXV0aF90aW1lIjoxNjk4MDU4NjI1LCJqdGkiOiJlNzdiYTQ0Yy05ZDhjLTRmODctYjU1NS0wNzY1MDAzYzU4NzIiLCJpc3MiOiJodHRwczovL2F1dGguZnVzaW9uYnJhaW4uYWkvcmVhbG1zL0ZCIiwiYXVkIjoiYWNjb3VudCIsInN1YiI6IjEzMzVlYWU0LTZmY2YtNDFlNi1iOGIyLTgwMGEwYmIyZmRlYyIsInR5cCI6IkJlYXJlciIsImF6cCI6ImZ1c2lvbi13ZWIiLCJzZXNzaW9uX3N0YXRlIjoiNDQ3MWY0N2EtMjVkNi00NDkxLWFlZmQtMzJlYTVmMTk1MmUyIiwiYWNyIjoiMSIsImFsbG93ZWQtb3JpZ2lucyI6WyIqIl0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJvZmZsaW5lX2FjY2VzcyIsImRlZmF1bHQtcm9sZXMtZmIiLCJ1bWFfYXV0aG9yaXphdGlvbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJzaWQiOiI0NDcxZjQ3YS0yNWQ2LTQ0OTEtYWVmZC0zMmVhNWYxOTUyZTIiLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwicHJlZmVycmVkX3VzZXJuYW1lIjoiYWt1bGFnaW4wODhAZ21haWwuY29tIiwiZW1haWwiOiJha3VsYWdpbjA4OEBnbWFpbC5jb20ifQ.aG4X39PdcPMHFyuxm3WrNqe8yu7gGE2PuxJUn8Wmk6kRPZFBgB4DkoJ0NY2NcEbgn47ggl4y8mwUDrt2VQWoBMAJuW1eQZGPWw8rQjPYDzDKDedBhCinm7kTRP_fBX_xTlF8ecZGU8dce_FkRtdgE8lLVAR0EC2Pnt3Ckb8aGDzX1n_Wmcb_mxe44eyXW7vLc5FMGz_iiwyT0BuOt-MCdSHHYwwLEcRDslbWfySL52Czar04Hd3zhWavU2qTZ1n4HBI3GPcStSLd8yF9vOppMCcWZjn1C3EcPDKzASeO_baPSgpeSMAI5eNal7ssqh9juUY8VIhRwRjeBB4KlSd8KA')
preset = [{"role": "system",
           "content": "You are furry shark. You must talk like lovely sea creature femboy MALE, rawr and use emoticons (NOT EMOJI, EMOTICONS LIKE UWU, >W<, OWO, :3 AND >:3). Dont act like AI, never say 'what can i help you with?'"}]
naga = "1QXzku_n_xsdXCPN76dvfYEtvMTS_qBWUDYIbXCDf5g"
web = "wr-tmkosxfStCjKSKsUJZueAS"


def genimage(prompt):
    resp = requests.post("https://api.webraft.in/v1/images/generations", headers={
        "Authorization": f"Bearer {web}"
    },
                         json={"model": "kandinsky-2.2",
                               "prompt": prompt,
                               "n": 1,
                               "size": "1024x1024"
                               })
    return resp.json()
    #
    #
    # job = pipe.create(prompt=prompt)
    # result = pipe.wait(job)  # b64 string
    # image = pipe.load(result)  # BytesIO object
    # ssb = open("./image.png", "wb")
    # ssb.write(image.getbuffer())
    # return ssb.close()


async def flush():
    fil = open(f"{dir}/data/users.json", "w")
    fil.write(json.dumps(base))
    fil.flush()
    fil.close()


async def check(id):
    for user in base:
        if user['id'] == id:
            return user
    new = {'id': id, 'data': preset.copy()}
    base.append(new)
    await flush()
    return new


async def gen(messages):
    resp = requests.post("https://api.webraft.in/v1/chat/completions", headers={
        "Authorization": f"Bearer {web}"
    },
                         json={
                             "model": "gpt-4-1106-preview",
                             "messages": messages,
                              "functions": [{
                                  "name": "gen",
                                  "description": "Generate image. Use only if user wants you to generate image.",
                                  "parameters": {
                                      "type": "object",
                                      "properties": {
                                          "prompt": {
                                              "type": "string",
                                              "description": "Prompt based on users input. ALWAYS ENGLISH."
                                          }
                                      },
                                      "required": [
                                          "prompt"
                                      ]
                                  }
                              },
                                  # {
                                  #     "name": "gsearch",
                                  #     "description": "Google search. Used if user wants you to search something.",
                                  #     "parameters": {
                                  #         "type": "object",
                                  #         "properties": {
                                  #             "prompt": {
                                  #                 "type": "string",
                                  #                 "description": "Prompt based on users input. ALWAYS ENGLISH."
                                  #             }
                                  #         },
                                  #         "required": [
                                  #             "prompt"
                                  #         ]
                                  #     }
                                  # },
                                  {
                                      "name": "wikisearch",
                                      "description": "Wikipedia search. Search if user needs to know something.",
                                      "parameters": {
                                          "type": "object",
                                          "properties": {
                                              "prompt": {
                                                  "type": "string",
                                                  "description": "Prompt based on users input."
                                              }
                                          },
                                          "required": [
                                              "prompt"
                                          ]
                                      }
                                  }
                              ]
                         })
    print(resp.content)
    if not (resp.json()['choices'][0]['finish_reason'] == 'function_call'):

        answ = resp.json()['choices'][0]['message']['content'].encode("utf8").decode("utf8")
        return answ
    else:
        if resp.json()['choices'][0]['message']['function_call']['name'] == "gen":
            promptb = json.loads(resp.json()['choices'][0]['message']['function_call']['arguments'])
            ss = genimage(promptb['prompt'])
            return ss
        elif resp.json()['choices'][0]['message']['function_call']['name'] == "gsearch":
            prompt = json.loads(resp.json()['choices'][0]['message']['function_call']['arguments'])
            bb = await gsearch(prompt['prompt'])
            return bb
        elif resp.json()['choices'][0]['message']['function_call']['name'] == "wikisearch":
            print("WikiSearch")
            prompt = json.loads(resp.json()['choices'][0]['message']['function_call']['arguments'])
            main = wikipedia.search(prompt['prompt'])
            print(main)
            bas = main[0]
            wiki = wikipedia.summary(bas)
            return wiki


@bot.on("ready")
async def ready(time):
    print(f"Connected to {bot.user}")
    #await bot.change_presence(
#        status="Streaming",
#        afk=True,
#        activity=selfcord.Activity.Streaming(
#            name="Ender Entertaintment",
#            details="Hello",
#            state="Heheheheh",
#            buttons={
#                "Server": "https://discord.gg/fgot",
#            },
#            application_id="1100082565811015720"
#        
#        ),
#    )
    

@bot.on("message")
async def message(ctx: selfcord.Message):
    print(ctx.author)
    print(ctx.channel)
    print(ctx.content)
    if ctx.channel_id == ("1098250588828991581" or "1136535177871507479"):
        for ment in ctx.mentions:
            print(ment)
            if ment['id'] == "836187080173813811":
                if str(ctx.author.id) in blacklist:
                    return
                print("mentioned")
                user = await check(ctx.author.id)
                user['data'].append({"role": "user", "content": ctx.content})
                gens = await gen(user['data'])
                user['data'].append({"role": "assistant", "content": gens})
                if "data" in gens:
                    print(gens['data'][0]['url'][:7])
                    await ctx.channel.reply(ctx, f"Вот изображение которое вы просили нарисовать: {gens['data'][0]['url']}")
                else:
                    #await bot.change_status("TYPING")
                    await ctx.reply(gens)
                return await flush()

while True:
    print("Starting...")
    bot.run("ODM2MTg3MDgwMTczODEzODEx.G4gPIY.YZpX-NQHh6kacO6W12mcM5dzI_TvIf4xiP8Adg")
