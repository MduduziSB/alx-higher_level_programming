#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include "lists.h"
/**
 * check_cycle - checks for loops in a singly linked list
 * @list: linked list's head
 * Return: 1 (has a cycle) 0 (has no cycle)
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp1 = list, *tmp2 = list;

	while (tmp1->next && tmp2->next->next)
	{
		tmp2 = tmp2->next->next;
		if (!tmp2->next)
			return (0);
		tmp1 = tmp1->next;
		if (!tmp2 || !tmp1)
			return (0);
		if (tmp2 == tmp1)
			return (1);
	}
	return (0);
}

