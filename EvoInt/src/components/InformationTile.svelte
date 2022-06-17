<script lang="ts">
	export let title: string;
	export let content: string = '';
	export let right_side: boolean = false;

	let className: string;
	export { className as class };
</script>

<div
	class={`container w-full flex ${
		right_side && 'flex-row-reverse'
	} justify-between items-center ${className}`}
>
	<div class={`w-1/2 max-w-2xl flex flex-col ${right_side && 'text-right'} gap-2`}>
		<p class="text-5xl mb-4 font-bold uppercase text-gray-100">{title}</p>
		{#if content}
			<p class="text-2xl text-justify text-gray-400">{content}</p>
		{:else}
			<slot name="content" />
		{/if}
		<slot name="left_slot" />
	</div>
	<div class="w-1/2">
		<slot name="right_slot" />
	</div>
</div>

<style lang="postcss">
	.container {
	}
</style>
