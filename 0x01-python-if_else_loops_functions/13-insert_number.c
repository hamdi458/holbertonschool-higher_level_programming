#include <stdlib.h>
#include "lists.h"
#include <string.h>
/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: var head.
 * @number: var number
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head;
	listint_t *nouveau;

	nouveau = malloc(sizeof(listint_t));
	if (!nouveau)
		return (NULL);
	nouveau->n = number;
	if (node == NULL || node->n >= number)
	{
		nouveau->next = node;
		*head = nouveau;
		return (nouveau);
	}
	while (node && node->next && node->next->n < number)
		node = node->next;
	nouveau->next = node->next;
	node->next = nouveau;
	return (nouveau);
}
