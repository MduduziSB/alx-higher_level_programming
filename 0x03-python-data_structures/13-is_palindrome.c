#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include "lists.h"
/**
 * size_of_list - computes size listint_t list
 * @h: pointer to listint_t list head
 * Return: number of nodes
 */
size_t size_of_list(const listint_t *h)
{
	const listint_t *ptr;
	size_t n;

	ptr = h;
	n = 0;
	while (ptr != NULL)
	{
		ptr = ptr->next;
		n++;
	}
	return (n);
}
/**
 * is_palindrome - checks if listint_t list is a palindrome
 * @head: pointer to listint_t list head
 * Return: 1 (is palindrome) 0(not palindrome)
 */
int is_palindrome(listint_t **head)
{
	size_t list_size, j = 0;
	int arr[2000];
	listint_t const *ptr = *head;

	list_size = size_of_list(ptr);
	if (!ptr || list_size == 1)
		return (1);

	while (j < list_size / 2)
	{
		arr[j] = ptr->n;
		ptr = ptr->next;
		j++;
	}
	j--;
	if (list_size % 3 == 0)
		ptr = ptr->next;
	while (ptr)
	{
		if (arr[j] != ptr->n)
			return (0);
		ptr = ptr->next;
		j--;
	}
	return (1);
}

