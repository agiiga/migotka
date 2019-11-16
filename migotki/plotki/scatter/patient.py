
import matplotlib.pyplot as plt

from dao import PATIENTS


def patients_currents(extensors_or_flexors):
    extensors = {'p2': [], 'p3': [], 'p4': [], 'p5': [], 'p6': [], 'p7': [], 'p8': [], 'p9': []}
    ps = list(extensors.keys())
    patients = [p for p in PATIENTS if p.name in ps]

    for p in patients:
        sessions = p.data['FES_parameters']
        for ix, session in enumerate(sessions):
            d = (ix+1, p.get_extensor(session) if extensors_or_flexors else p.get_flexor(session))
            extensors[p.name].append(d)

    markers = dict(zip(ps, [".", "d", "o", "x", "D", "p", "s", "*"]))

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, facecolor="1.0")

    for p, data in extensors.items():
        session, currents = zip(*data)
        marker = markers[p]
        ax.scatter(session, currents, alpha=0.8, edgecolors='none', s=30, marker=marker, label=p)

    ax.set_xlabel('Session Number')
    ax.set_ylabel('Current (mA)')

    title = "extensors" if extensors_or_flexors else "flexors"
    plt.title("All Patients " + title + " Currents")
    plt.legend(loc=5)
    plt.show()


def plot_all_patients_extensors_currents():
    patients_currents(True)


def plot_all_patients_flexors_currents():
    patients_currents(False)


