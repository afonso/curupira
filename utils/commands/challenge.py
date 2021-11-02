from ..database.setup import Challenge, Attempt
import utils.logging.log as log
import discord

def get_challenges(ctx):
    """
    Essa funcao retorna todos os challenges cadastrados no CTF
    """
    try:
        challenges = Challenge.select(Challenge.id,
                                      Challenge.name, 
                                      Challenge.points, 
                                      Challenge.category, 
                                      Challenge.description,
                                      Challenge.url).join(Attempt, on=(Challenge.id == Attempt.chall_id)).where(Attempt.correct == False)
        challs = ""
        for challenge in challenges.iterator(): 
            challs += f'''{challenge.name} ({challenge.id}) - {challenge.points} Pontos - {challenge.category}
                          {challenge.description}
                          {challenge.url}
                       ------------------------------------------------------------
                       '''
            for challenge in challenges.iterator()
        )

        return discord.Embed(title="Challeges", description=challs)
    except Exception as err:
        log.err(err)