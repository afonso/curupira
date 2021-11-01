from ..database.setup import Attempt, Challenge
from datetime import datetime


def check_flag(challId, flag, userId):
    """
    Essa funcao verifica se a flag esta correta, criando sempre um Attempt

    @Params
    :challId => ID da Challenge
    :flag => flag do Challenge
    :userId => ID do Usuario
    """
    if Attempt.select(Attempt.flag).where(
                                            Attempt.correct == True,
                                            Attempt.user_id == userId,
                                            Attempt.chall_id == challId
                                          ).count() > 0:
        return "Você já submeteu a flag para esse desafio!"

    challInfo = Challenge.select().where(Challenge.id == challId)

    print(dir(challInfo))

    test = [Challenge.select().where(Challenge.id == challId)]
    print(f"test: {test}")

    teste2 = [Challenge.select().where(Challenge.id == challId)]
    test2 = [i for i in teste2] 
    print(f"test2: {test2}")

    Attempt.create(
            user_id=userId,
            chall_id=challId,
            flag=flag,
            correct=True if challInfo.flag == flag else False,
            timestamp=datetime.timestamp()
        )

    if challInfo.flag == flag:
        return f"Parabéns!!! Você resolveu o desafio {challInfo.name}!"

    return "Flag incorreta!"


# a = Attempt.select(Attempt.flag)
# result = [i for i in a]
