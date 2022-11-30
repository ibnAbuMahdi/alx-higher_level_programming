#include "lists.h"
#include <stddef.h>
#include <stdlib.h>

/**
 * check_cycle - find the beginning of a loop if exist
 * @h: pointer to the head node
 * Return: 0 if no cycle found and 1 o.w.
 */

int check_cycle(listint_t *h)
{
	listint_t *slow_p = h, *fast_p = h;

	while (slow_p && fast_p && fast_p->next)
	{
		slow_p = slow_p->next;
		fast_p = fast_p->next->next;
		if (slow_p == fast_p)
			return (1);
	}
	return (0);
}
