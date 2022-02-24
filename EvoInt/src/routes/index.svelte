<script lang="ts">
	import Button from '../components/Button.svelte';
	import { goto } from '$app/navigation';
	import Header from '../components/Header.svelte';

	let name: string = 'Test';
	let show: boolean = false;

	function onClick() {
		show = !show;
	}

	function navHelp() {
		goto('/help');
	}
</script>

<Header />
<h1>EVOINT</h1>

<style lang="postcss">
</style>
