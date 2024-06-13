/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_calloc.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: krybalch <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/01/22 18:08:04 by krybalch          #+#    #+#             */
/*   Updated: 2023/02/06 14:24:23 by krybalch         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_calloc(size_t count, size_t size)
{
	char	*str;
	size_t	i;

	i = count * size;
	if (count == 0 || size == 0)
	{
		str = malloc(0);
		return (str);
	}
	if (i / count != size)
		return (0);
	str = malloc(i);
	if (!str)
		return (0);
	ft_bzero(str, i);
	return (str);
}
