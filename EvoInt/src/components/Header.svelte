<script>
	import NavigationButton from './NavigationButton.svelte';
</script>

<header>
	<img src="logo.png" width="200px" alt="EvoInt-Logo" />
	<div id="navigation">
		<NavigationButton text="Tutorial" href="tutorial" />
		<NavigationButton text="Über uns" href="about_us" />
	</div>
</header>

<style lang="postcss">
	header {
		@apply font-evoint p-4 w-full flex items-center gap-5 bg-gray-800 text-gray-200;
	}

	p {
		@apply text-3xl;
	}

	#navigation {
		@apply flex gap-5;
	}
</style>
