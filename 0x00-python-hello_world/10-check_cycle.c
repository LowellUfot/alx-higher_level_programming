#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to singly linked list
 *
 * Return: 0 if there is no cycle, 1 if there is cycle
 *
 */
int check_cycle(listint_t *list)
{
	listint_t *check1, *check2;

	check1 = list;
	check2 = list;

	while (check1 && check2)
	{
		if (check2->next == NULL)
			return (0);
		check1 = check1->next;
		check2 = check2->next->next;
		if (check1 == check2)
			return (1);
	}
	return (0);
}
