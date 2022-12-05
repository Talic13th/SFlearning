def confidence_interval(n, x_mean, sigma, gamma=0.95, digits=2):
        """Calculation confidence interval
            X_mean = +/-z_crit * (sigma/n**0.5)

        Args:
            n (int): sample size
            x_mean (float): sample mean
            sigma (float): true standard deviation
            gamma (float, optional): reliability level. Default is 0.95
            digits (int, optional): the number of decimals to use when
                                    rounding the number. Default is 2
            
        Returns:
            confidence_interval (tuple): rounded confidence interval bounds
        """
        from scipy.stats import norm
        
        alpha = 1 - gamma
        z_crit = -norm.ppf(alpha/2) 
        eps = z_crit * sigma/(n ** 0.5) #error
        lower_bound = x_mean - eps # left (bottom) border
        upper_bound = x_mean + eps # right (top) border
        confidence_interval = (round(lower_bound, digits),
                            round(upper_bound, digits)) 
        return confidence_interval
 
    
def t_distribution(n, x_mean, x_std, gamma=0.95, digits=2):
    """Calculation "t"-distribution
        X_mean = +/-t_crit * (x_std/n**0.5)

    Args:
        n (int): sample size
        x_mean (float): sample mean
        x_std (float): sample standard deviation
        gamma (float, optional): reliability level. Default is 0.95
        digits (int, optional): the number of decimals to use when
                                rounding the number. Default is 2
        
    Returns:
        t_distribution (tuple): rounded "t"-distribution bounds
    """
    from scipy.stats import t
    
    alpha = 1 - gamma
    k = n - 1
    t_crit = -t.ppf(alpha/2, k)
    eps = t_crit * x_std/(n ** 0.5) # error
    lower_bound = x_mean - eps # left (bottom) border
    upper_bound = x_mean + eps # right (top) border
    t_distribution = (round(lower_bound, digits),
                      round(upper_bound, digits)) 
    return t_distribution


def proportions_conf_interval(n, x_p, gamma=0.95, digits=2): 
    """Calculation confidence interval for proportions
         = +/-z_crit * (x_p(1 - xp)/n**0.5)

    Args:
        n (int): sample size
        x_p (float): sample proportion
        gamma (float, optional): reliability level. Default is 0.95
        digits (int, optional): the number of decimals to use when
                                rounding the number. Default is 2
        
    Returns:
        Confidence interval for proportion, %
    """  
    from scipy.stats import norm
    
    alpha = 1 - gamma 
    z_crit = -norm.ppf(alpha/2) # z критическое
    eps = z_crit * (x_p * (1 - x_p) / n) ** 0.5 # error
    lower_bound = x_p - eps # left (bottom) border
    upper_bound = x_p + eps # right (top) border
    return round(lower_bound * 100, digits), round(upper_bound * 100, digits)
 
    
def diff_proportions_conf_interval(n, xp, gamma=0.95, digits=2):
    """Calculation confidence interval of proportions difference
         
    Args:
        n (list): list of sample size for A and B
        xp (list): list of sample proportion for A and B respectively
        gamma (float, optional): reliability level. Default is 0.95
        digits (int, optional): the number of decimals to use when
                                rounding the number. Default is 2
        
    Returns:
        Confidence interval interval of proportions difference, %
    """  
    from scipy.stats import norm
    
    alpha = 1 - gamma 
    diff = xp[1] - xp[0] # sample difference of convertions for groups A and B
    z_crit = -norm.ppf(alpha/2)
    eps = z_crit * (xp[0] * (1 - xp[0])/n[0] + xp[1] * (1 - xp[1])/n[1]) ** 0.5
    lower_bound = diff - eps # left (bottom) border
    upper_bound = diff + eps # right (top) border
    
    return round(lower_bound *100, digits), round(upper_bound * 100, digits)    
