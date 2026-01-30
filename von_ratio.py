import scipy
from scipy import stats
import numpy 

def compute_von_neumann_ratio(data, alpha, verbose=False):
    """
    The von-Neumann ratio test is a statistical test designed for testing the
    independence of subsequent observations.
    The null hypothesis is that the data are independent and normally
    distributed.

    Input:
        alpha: Significance level.

    Return:
        von neumann ratio

    References: 
        von Neumann (1941)
        Used in Kalari et al. (2026, A&A)
    """

    mean_square_successive_difference = np.power(np.ediff1d(data), 2).mean()
    von_neumann_ratio = mean_square_successive_difference / data.var()
    von_neumann_mean = 2.
    von_neumann_var = 4. * (data.size - 2.) / (data.size ** 2 - 1.)
    acceptance_region = scipy.stats.norm.interval(
        1.0 - alpha,
        loc=von_neumann_mean,
        scale=np.sqrt(von_neumann_var)
    )

    if verbose:
        print(
            (
                "von Neumann ratio v = {:.2f},\n"
                "acceptance region at {:.0f}% significance level is "
                "({:.2f}, {:.2f})"
            ).format(
                von_neumann_ratio,
                alpha * 100,
                acceptance_region[0],
                acceptance_region[1]
            )
        )

    return (1/von_neumann_ratio)
