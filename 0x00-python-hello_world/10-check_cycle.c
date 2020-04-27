#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: var list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *i, *j;

	i = list;
	j = list;
	if (!i)
		return (0);
	while (i && (i = i->next))
	{
		if (i == j)
			return (1);
		i = i->next;
		if (i == n)
			return (1);
		j = j->next;
	}
	return (0);
}
