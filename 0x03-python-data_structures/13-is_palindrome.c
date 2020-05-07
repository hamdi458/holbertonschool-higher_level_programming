#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * get_node - search node
 * @pos: var pos int
 * @head:var head
 * Return: node at this pos
 */

listint_t *get_node(int pos, listint_t *head)
{
	int i = 0;

	while (i < pos)
	{
		head = head->next;
		i++;
	}
	return (head);
}


/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to list to be checked
 * Return: 0  if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *node = *head, *start = NULL, *end = NULL;
	int l = 0, i;

	if (*head == NULL)
		return (1);
	while (node != NULL)
	{
		node = node->next;
		l++;
	}
	if (l == 1)
		return (0);
	if (l == 0)
		return (0);
	start = *head;
	end = *head;
	for (i = 0; i < l / 2; i++)
	{
		end = get_node(l - i - 1, *head);
		if (start->n != end->n)
			return (0);
		start = start->next;
	}
	return (1);
}
