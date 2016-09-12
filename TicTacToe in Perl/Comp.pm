package Comp;
use strict;
use warnings;
use Player;

our @ISA = "Player";

my @List = (0,1,2,3,4,5,6,7,8);

sub new          # Constructor
{
	my $class = shift;
	my $self = {};
	bless($self, $class);
	return $self;
}

sub fill
{
	my ($self) = @_;
	print "\nThe Computer is playing! ";
	my $range = (scalar @List) - 1;
	my $ip = int(rand($range));
	while ($Player::Array[$List[$ip]] ne ""){	
		splice (@List,$ip,1);
		$range = (scalar @List) - 1;
		my $ip = int(rand($range));
	}
	$Player::Array[$List[$ip]] = "O";
	splice (@List,$ip,1);
	$range = (scalar @List) - 1;
	$Player::count -= 1;
}
