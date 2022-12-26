#include "lists.h"
#include <stdlib.h>
#include <stddef.h>

/**
 * listint_len - finds the length of a linkedlist
 * @h: the head node
 * Return: the length or 0 if empty list
 */

size_t listint_len(const listint_t *h)
{
	if (h == NULL)
		return (0);
	else
		return (1 + listint_len(h->next));
}

/**
 * is_palindrome - check whether a linkedlist is palindrome
 * @h: the address of the head node
 * Return: 1 if palindrome, 0 o.w.
 */

int is_palindrome(listint_t **h)
{
	size_t len;

	if (!h)
		return (0);
	len = listint_len(*h);

	if (len == 1 || len == 0)
		return (1);
	return (compare(*h, 0, len - 1, 0));
}

/**
 * compare - compare two nodes
 * @h: the head node
 * @i: index of first node
 * @f: index of second node
 * @d: no. of nodes traversed
 * Return: 1 if they are equal else 0
 */

int compare(listint_t *h, int i, int f, int d)
{
	listint_t *node_i, *node_f;

	if (i == f)
		return (1);

	node_i = get_nodeint_at_index(h, i - d);
	node_f = get_nodeint_at_index(h, f - d);

	if (i == f - 1)
		return (node_i->n == node_f->n);
	if (node_i->n != node_f->n)
		return (0);
	d++;
	return (compare(h->next, i + 1, f - 1, d));
}

/**
 * get_nodeint_at_index - gets node at index
 * @head: the head node
 * @index: index of node
 * Return: the node at index or NULL if index is out of range
 */

listint_t *get_nodeint_at_index(listint_t *head, unsigned int index)
{
	unsigned int i = 0;
	listint_t *temp = NULL;

	if (head)
	{
		temp = head;
		while (temp)
		{
			if (i == index)
				return (temp);
			i++;
			temp = temp->next;
		}
	}
	return (NULL);
}
