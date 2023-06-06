#include <stdlib.h>
#include <stddef.h>
#include <stdio.h>
#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: linked list's head
 * @number: new node's data
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *ptr = *head, *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;

	if (ptr)
	{
		if (new->n < ptr->n)
		{
			new->next = ptr;
			*head = new;
			return (new);
		}
		while (ptr)
		{
			if (new->n >= ptr->n)
			{
				if (ptr->next == NULL || new->n < (ptr->next->n))
				{
					new->next = ptr->next;
					ptr->next = new;
					return (new);
				}
			}
			ptr = ptr->next;
		}
	}
	return (NULL);
}

