#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle -  a function in C that checks if a singly linked
 * list has a cycle in it.
 * @list: pointer to list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fixed;
	listint_t *current;

	fixed = list;
	current = list;
	while (current != NULL)
	{
		current = current->next;
		if (fixed == current)
		{
			return (1);
		}
	}
	return (0);
}
