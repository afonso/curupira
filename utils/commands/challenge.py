from ..database.setup import Challenge, Attempt, User
import utils.logging.log as log
import discord


def get_challenges(ctx):
    """
    Essa funcao retorna todos os challenges cadastrados no CTF
    """
    try:
        print('=====> vai pegar o user')
        user = User.get(User.discordId == ctx.author.id)
        print('=====> terminou de pegar o user')

        print('=====> vai pegar a challenge')
        challenges = Challenge.select(
                                    Challenge.id,
                                    Challenge.name,
                                    Challenge.points,
                                    Challenge.category,
                                    Challenge.description,
                                    Challenge.url
                                    )
        print('=====> terminou de pegar a challenge')

        print('=====> vai pegar a attempt')
        attempts = Attempt.select().where(Attempt.correct == True, Attempt.user_id == user.id)
        print('=====> terminou de pegar a attempt')

        challs = ""

        for challenge in challenges:
            if len(attempts) >= 1:
                print('O USER TEM ATTEMPT')
                for attempt in attempts:
                    print(dir(attempt))
                    print("#*" * 30)
                    print(f"<> <> <>Attempt: {attempt}")
                    print("#*" * 30)
                    print(challenge.id)
                    print(attempt.id)
                    if challenge.id == attempt.chall_id:
                        print(f"Challenges = {type(challenges)} = {challenges}")
                        print("&" * 30)
                        print(f"Challenge = {type(challenge)} = {challenge}")
                        challenges.remove(challenge)
            challs += f'''{challenge.name} ({challenge.id}) - {challenge.points} Pontos - {challenge.category}
                          {challenge.description}
                          {challenge.url}
                       ------------------------------------------------------------
                       '''
        return discord.Embed(title="Challenges", description=challs)
    except Exception as err:
        log.err(err)
