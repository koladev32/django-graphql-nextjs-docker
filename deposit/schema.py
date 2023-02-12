import graphene

from graphene_django import DjangoObjectType

from deposit.models import Deposit


class DepositType(DjangoObjectType):
    class Meta:
        model = Deposit
        fields = ('id', 'amount', 'reference', 'depositor', 'date')


class DepositQuery(graphene.ObjectType):
    all_deposits = graphene.List(DepositType)

    def resolve_all_deposits(self, root, info):
        return Deposit.objects.all()


schema = graphene.Schema(query=DepositQuery)
