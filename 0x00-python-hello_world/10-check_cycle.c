#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checkts if the linked list has a cycle
 *
 * @list: the pointer to the linked list
 *
 * Return: 1 if cycle, 0 otherwise
*/

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (fast && fast->next && slow)
	{
		slow = slow->next;
		fast =  fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
