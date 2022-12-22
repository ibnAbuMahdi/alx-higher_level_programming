#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * insert_node - inserts a node in a sorted list
 * @head: the address of the pointer to the head
 * @num: the num of the new node
 * Return: the address of the new node or NULL if it fails
 */

listint_t *insert_node(listint_t **head, int num)
{
	listint_t *temp = NULL, *prev = NULL, *new = NULL;

	if (head)
	{
		new = malloc(sizeof(listint_t));
		if (!new)
			return (NULL);
		new->n = num;
		if (*head)
		{
			temp = *head;
			while (temp && temp->n < num)
			{
				prev = temp;
				temp = temp->next;
			}
			if (prev)
			{
				prev->next = new;
				new->next = temp;
			}
			else
			{
				new->next = temp;
				*head = new;
			}
		}
		else
		{
			new->next = NULL;
			*head = new;
		}
	}
	return (new);
}
