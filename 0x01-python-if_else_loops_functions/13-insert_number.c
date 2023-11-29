#include "lists.h"
#include <stdlib.h>

/**
 * add_nodeint_end - insert the node repectively
 *
 * @head: the head of the linked list
 * @n: the data of the linked list
 *
 * Return: the node or null
*/




listint_t *add_nodeint_end(listint_t **head, int number)
{
	listint_t *node = *head, *new = malloc(sizeof(listint_t));

	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (!node || new->n < node->n)
	{
		new->next = node;
		return (*head = new);
	}

	while (node)
	{
		if (!node->next || new->n < node->next->n)
		{
			new->next = node->next;
			node->next = new;
			return (node);
		}
		node = node->next;
	}
	return (NULL);
}
