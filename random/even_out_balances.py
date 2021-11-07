from typing import List, Tuple


def even_balances(balances: List[int]):
    goal_balance = sum(balances) // len(balances)
    print(f"Goal balance for all accounts is {goal_balance}$")

    transfers = []
    for account_id, balance in enumerate(balances):
        transfers.extend(
            transfer_money_from_accounts(account_id, goal_balance, balances)
        )

    return transfers


def transfer_money_from_accounts(
        destination_account_id: int,
        transfer_upperbound_threshold: int,
        balances: List[int],
) -> List[Tuple[int, int, int]]:
    to_withdraw = transfer_upperbound_threshold - balances[destination_account_id]

    if to_withdraw <= 0:
        return []

    withdraw_transfers = []
    for account_id, balance in enumerate(balances):
        if account_id == destination_account_id:
            continue

        if balance > transfer_upperbound_threshold:
            withdraw_amount = min(balance - transfer_upperbound_threshold, to_withdraw)
            balances[account_id] -= withdraw_amount
            balances[destination_account_id] += withdraw_amount
            to_withdraw -= withdraw_amount
            withdraw_transfers.append((account_id, destination_account_id, withdraw_amount))

        if balances[destination_account_id] >= transfer_upperbound_threshold:
            break

    return withdraw_transfers


if __name__ == '__main__':
    balances = [500, -20, 50, 170, 100, 240, -100]
    print(f"List of transfers to even out balances (from, to, amount): {even_balances(balances)}")
    print(f"Balances after all transfers: {balances}")
