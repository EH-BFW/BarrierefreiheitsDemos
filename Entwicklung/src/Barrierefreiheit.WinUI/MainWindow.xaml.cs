using System;
using Microsoft.UI.Xaml;
using Microsoft.UI.Xaml.Controls;
using Barrierefreiheit.WinUI.Pages;

namespace Barrierefreiheit.WinUI;

public sealed partial class MainWindow : Window
{
    public MainWindow()
    {
        InitializeComponent();
        Title = "BFW Würzburg – Barrierefreiheit (WinUI 3)";
        ContentFrame.Navigate(typeof(HomePage));
        NavView.SelectedItem = NavView.MenuItems[0];
    }

    private void NavView_SelectionChanged(NavigationView sender, NavigationViewSelectionChangedEventArgs args)
    {
        if (args.SelectedItem is not NavigationViewItem item) return;

        Type? page = item.Tag switch
        {
            "home"      => typeof(HomePage),
            "barrieren" => typeof(BarrierenPage),
            "loesungen" => typeof(LoesungenPage),
            "ueber"     => typeof(UeberPage),
            _ => null
        };
        if (page is not null)
            ContentFrame.Navigate(page);
    }
}
