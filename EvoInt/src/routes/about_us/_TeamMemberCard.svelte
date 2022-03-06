<script lang="ts">
	import Icon from '../../components/Icon.svelte';

	export let icons: string[] = [];
	export let name: string;
	export let description: string = '';
</script>

<div id="content">
	<div id="up">
		{#each icons as icon}
			<Icon {icon} />
		{/each}
		<p id="name-p">{name}</p>
	</div>
	<div id="bottom">
		<p id="description-p">{description}</p>
	</div>
</div>

<style lang="postcss">
	#content {
		@apply w-fit p-2 flex flex-col bg-gray-900 rounded-md;
	}
	#up {
		@apply px-2 flex items-center gap-2;
	}
	#name-p {
		@apply text-white font-bold text-2xl;
	}
	#bottom {
	}
	#description-p {
		@apply text-gray-300 text-xl;
	}
</style>
