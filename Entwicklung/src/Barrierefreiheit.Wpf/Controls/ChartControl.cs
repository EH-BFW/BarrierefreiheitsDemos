using System.Windows;
using System.Windows.Automation.Peers;
using System.Windows.Controls;
using System.Windows.Input;

namespace Barrierefreiheit.Wpf.Controls;

/// <summary>
/// Tab-fokussierbarer Container für eigene Diagramme.
///
/// Ein nacktes <see cref="Border"/> mit <c>AutomationProperties.Name</c>
/// erscheint im UIA-Tree zwar als generischer Knoten, hat aber keine
/// aussagekräftige Rolle. Screenreader wie JAWS überspringen solche
/// Elemente oder sagen nur "Bereich" an. Über einen eigenen
/// <see cref="AutomationPeer"/> exponieren wir das Control als
/// <see cref="AutomationControlType.Image"/> – damit erscheint es als
/// echte Grafik im Sprach- und Braille-Output.
/// </summary>
public class ChartControl : ContentControl
{
    static ChartControl()
    {
        // Per Default fokussierbar und Tab-stoppbar machen
        FocusableProperty.OverrideMetadata(
            typeof(ChartControl), new FrameworkPropertyMetadata(true));
        KeyboardNavigation.IsTabStopProperty.OverrideMetadata(
            typeof(ChartControl), new FrameworkPropertyMetadata(true));
    }

    protected override AutomationPeer OnCreateAutomationPeer()
        => new ChartControlAutomationPeer(this);
}

/// <summary>
/// AutomationPeer für <see cref="ChartControl"/> mit Rolle "Image".
/// </summary>
public class ChartControlAutomationPeer : FrameworkElementAutomationPeer
{
    public ChartControlAutomationPeer(FrameworkElement owner) : base(owner) { }

    protected override AutomationControlType GetAutomationControlTypeCore()
        => AutomationControlType.Image;

    protected override string GetClassNameCore() => "Chart";

    /// <summary>
    /// Sicherstellen, dass das Control im UIA-Tree als eigener Knoten
    /// auftaucht und nicht als rein dekoratives Element ignoriert wird.
    /// </summary>
    protected override bool IsControlElementCore() => true;
    protected override bool IsContentElementCore() => true;
}
