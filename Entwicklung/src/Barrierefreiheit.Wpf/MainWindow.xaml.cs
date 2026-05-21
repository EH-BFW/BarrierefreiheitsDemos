using System.Windows;
using Barrierefreiheit.Wpf.Pages;

namespace Barrierefreiheit.Wpf;

public partial class MainWindow : Window
{
    public MainWindow()
    {
        InitializeComponent();
        Loaded += (_, _) => ContentFrame.Navigate(new HomePage());
    }

    private void Nav_Home_Click(object sender, RoutedEventArgs e)
        => ContentFrame.Navigate(new HomePage());

    private void Nav_Barrieren_Click(object sender, RoutedEventArgs e)
        => ContentFrame.Navigate(new BarrierenPage());

    private void Nav_Loesungen_Click(object sender, RoutedEventArgs e)
        => ContentFrame.Navigate(new LoesungenPage());

    private void Nav_Ueber_Click(object sender, RoutedEventArgs e)
        => ContentFrame.Navigate(new UeberPage());
}
