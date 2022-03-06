<script>
	import { goto } from '$app/navigation';

	import NavigationButton from './NavigationButton.svelte';

	function onHome() {
		goto('/');
	}
</script>

<header>
	<!--<img src="logo.png" width="200px" alt="EvoInt-Logo" />-->
	<p on:click={onHome}>EvoInt</p>
	<div id="navigation">
		<NavigationButton text="Tutorial" href="tutorial" />
		<NavigationButton text="Über uns" href="about_us" />
	</div>
</header>

<style lang="postcss">
	header {
		@apply font-evoint p-4 w-full flex items-center gap-5 bg-black text-gray-200;
	}

	p {
		@apply text-3xl hover:cursor-pointer;
	}

	#navigation {
		@apply flex gap-5;
	}
</style>
