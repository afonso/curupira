import utils.logging.log as log

from ..database.setup import Attempt, Challenge
import peewee


def check_flag(challId, flag, userId):
    """
    Essa funcao verifica se a flag esta correta, criando sempre um Attempt

    @Params
    :challId => ID da Challenge
    :flag => flag do Challenge
    :userId => ID do Usuario
    """
    try:
        chall = Challenge.get_by_id(challId)
    except Exception as e:
        log.err(e)
        return "Esse challenge id não existe!"

    try:
        Attempt.get(Attempt.correct == True, Attempt.user_id == userId, Attempt.chall_id == challId)
        return "Você já submeteu a flag desse desafio!"
    except peewee.DoesNotExist as e:
        log.err(e)
    
    if chall.flag == flag:
        try:
            Attempt.create(flag=flag, correct=True) # user_id=userId, chall_id=challId,
            return "Flag correta!"
        except Exception as e:
            log.err(e)
            return "Erro ao criar Attempt True"
    else:
        try:
            Attempt.create(flag=flag, correct=False) # user_id=userId, chall_id=challId, 
            return "Flag incorreta!"
        except Exception as e:
            log.err(e)
            return "Erro ao criar Attempt False"



# a = Attempt.select(Attempt.flag)
# result = [i for i in a]
