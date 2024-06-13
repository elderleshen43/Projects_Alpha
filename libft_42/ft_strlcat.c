/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: krybalch <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/01/22 18:06:04 by krybalch          #+#    #+#             */
/*   Updated: 2023/01/22 18:06:07 by krybalch         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

size_t	ft_strlcat(char *dst, const char *src, size_t size)
{
	size_t	i;
	size_t	j;
	size_t	strlen;

	i = 0;
	j = 0;
	strlen = ft_strlen(src);
	if (!dst && size == 0)
		return (strlen);
	while (dst[i] && i < size)
		i++;
	if (size > 0)
	{
		while (src[j] && i + 1 < size)
		{
			dst[i++] = src[j++];
		}
	}
	if (j > 0)
	{
		dst[i] = '\0';
		return (strlen + i - j);
	}
	return (strlen + i);
}
